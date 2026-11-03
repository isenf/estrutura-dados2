package red_black;


public class RedBlack <Key extends Comparable<Key>, Value> {
    private final Node<Key, Value> NIL;
    protected Node<Key, Value> root;
    protected int size;

    public RedBlack(){
        NIL = new Node<>();
        NIL.setRed(false);
        NIL.setParent(null);
        NIL.setLeft(NIL);
        NIL.setRight(NIL);
        this.root = NIL;
        this.size = 0;
    }

    public int size(){
        return this.size;
    }

    public boolean isEmpty(){
        return this.size == 0;
    }

    public Node<Key, Value> minNode(){
        Node<Key, Value> n = minNode(root);
        return n == NIL ? NIL : n;
    }

    private Node<Key, Value> minNode(Node<Key, Value> n){
        while (n.getLeft() != NIL) {
            n = n.getLeft();
        }
        return n;
    }

    public Node<Key, Value> maxNode(){
        Node<Key, Value> n = maxNode(root);
        return  n == NIL ? NIL : n;
    }

    private Node<Key, Value> maxNode(Node<Key, Value> n){
        while (n.getRight() != NIL) {
            n = n.getRight();
        }
        return n;
    }

    private boolean isRed(Node<Key, Value> node){
        return node != null && node.isRed();
    }

    private boolean isBlack(Node<Key, Value> node){
        return !isRed(node);
    }
    
    // search
    protected Node<Key, Value> searchNode(Key key){
        Node<Key, Value> cur = this.root;

        while (cur != NIL) {
            int comp = key.compareTo(cur.getKey());

            if(comp <0){
                cur = cur.getLeft();
            } else if(comp > 0){
                cur = cur.getRight();
            } else{
                return cur;
            }
        }

        return NIL; // node not found
    }

    public Value search(Key key){
        Node<Key, Value> node = searchNode(key);
        return node == this.NIL ? null : node.getValue();
    }

    public boolean contains(Key key){
        return searchNode(key) != this.NIL;
    }

    // rotations
    private void rotateLeft(Node<Key, Value> x){
        Node<Key, Value> y = x.getRight();
        x.setRight(y.getLeft());
        y.getLeft().setParent(x);
        y.setParent(x.getParent());

        if(x.getParent() == NIL){   // root case
            root = y;
        } else if(x == x.getParent().getLeft()){ // left child case
            x.getParent().setLeft(y);
        } else{ // right child case
            x.getParent().setRight(y);
        }

        y.setLeft(x);
        x.setParent(y);
    }

    private void rotateRight(Node<Key, Value> x){
        Node<Key, Value> y = x.getLeft();
        x.setLeft(y.getRight());
        y.getRight().setParent(x);
        y.setParent(x.getParent());

        if(x.getParent() == NIL){   // root case
            this.root = y;
        } else if(x.getParent().getLeft() == x){    // left child case
            x.getParent().setLeft(y);
        } else{ // right child case
            x.getParent().setRight(y);
        }

        y.setRight(x);
        x.setParent(y);
    }

    // insertion
    public void insert(Key key, Value value){
        Node<Key, Value> parent = this.NIL;
        Node<Key, Value> cur = this.root;
        int comp = 0;

        while (cur != this.NIL) {
            parent = cur;
            comp = key.compareTo(cur.getKey());

            if(comp < 0){
                cur = cur.getLeft();
            } else if(comp > 0){
                cur = cur.getRight();
            } else{
                cur.setValue(value);
                return;
            }
        }

        Node<Key, Value> z = new Node<>(key, value);
        z.setRight(this.NIL);
        z.setLeft(this.NIL);
        z.setParent(parent);

        if(parent == this.NIL){
            this.root = z;
        } else if(comp < 0){
            parent.setLeft(z);
        } else{
            parent.setRight(z);
        }

        this.size++;
        insertFixup(z);
    }

    private void insertFixup(Node<Key, Value> z){
        while (isRed(z.getParent())) {
            Node<Key, Value> p = z.getParent();
            Node<Key, Value> g = p.getParent();

            if(p == g.getLeft()){// z's parent is the left child 
                Node<Key, Value> u = g.getRight();  // z's uncle

                if(isRed(u)){   // z's uncle is red, case 1
                    p.setRed(false);
                    u.setRed(false);
                    g.setRed(true);
                    z = g;  // two levels up
                } else{
                    if(z == p.getRight()){  // z is p's right child, case 2: left rotation and case 3
                        z = p;
                        rotateLeft(z);
                        p = z.getParent();
                        g = p.getParent();
                    }
                    // case 3
                    p.setRed(false);
                    g.setRed(true);
                    rotateRight(g);
                }
            } else{ // z's parent is the right child, symmetric with left child case
                Node<Key, Value> u = g.getLeft();   // z's uncle
                if(isRed(u)){
                    p.setRed(false);
                    u.setRed(false);
                    g.setRed(true);
                    z = g;  // two levels up
                } else{
                    if(z == p.getLeft()){   // z is p's left child
                        z = p;
                        rotateRight(z);
                        p = z.getParent();
                        g = p.getParent();
                    }
                    p.setRed(false);
                    g.setRed(true);
                    rotateLeft(g);
                }
            }
        }
        this.root.setRed(false);
    }

    // deletion
    private void transplant(Node<Key, Value> u, Node<Key, Value> v){
        if(u.getParent() == this.NIL)  
            root = v;
        else if(u == u.getParent().getLeft())
            u.getParent().setLeft(v);
        else
            u.getParent().setRight(v);

        v.setParent(u.getParent());
    }

    public void delete(Key key){
        Node<Key, Value> z = searchNode(key);
        if(z == NIL)
            return; // node not found
        this.size--;

        Node<Key, Value> y = z;
        boolean yOriginalRed = y.isRed();
        Node<Key, Value> x;

        if(z.getLeft() == NIL){ // one child cases
            x = z.getRight();
            transplant(z, z.getRight());
        } else if(z.getRight() == NIL){
            x = z.getLeft();
            transplant(z, z.getLeft());
        } else{ // two child case
            y = minNode(z.getRight());
            yOriginalRed = y.isRed();
            x = y.getRight();
            if(y.getParent() == z){
                x.setParent(y);
            } else{
                transplant(y, y.getRight());
                y.setRight(z.getRight());
                y.getRight().setParent(y);
            }
            transplant(z, y);
            y.setLeft(z.getLeft());
            y.getLeft().setParent(y);
            y.setRed(z.isRed());
        }

        if(!yOriginalRed)
            deleteFixup(x);
    }

    private void deleteFixup(Node<Key, Value> x){
        while(x != root && isBlack(x)){
            if(x == x.getParent().getLeft()){   // x is the left child
                Node<Key, Value> w = x.getParent().getRight();
                if(isRed(w)){   // case 1
                    w.setRed(false);
                    x.getParent().setRed(true);
                    rotateLeft(x.getParent());
                    w = x.getParent().getRight();
                }

                if(isBlack(w.getLeft()) && isBlack(w.getRight())){  // case 2
                    if(w != NIL) w.setRed(true);
                    x = x.getParent();
                } else{
                    if(isBlack(w.getRight())){  // case 3
                        w.getLeft().setRed(false);
                        w.setRed(true);
                        rotateRight(w);
                        w = x.getParent().getRight();
                    }
                    w.setRed(x.getParent().isRed());    // case 4
                    x.getParent().setRed(false);
                    w.getRight().setRed(false);
                    rotateLeft(x.getParent());
                    x = root;
                }
            } else{ // its symmetrical
                Node<Key, Value> w = x.getParent().getLeft();
                if(isRed(w)){
                    w.setRed(false);
                    x.getParent().setRed(true);
                    rotateRight(x.getParent());
                    w = x.getParent().getLeft();
                }

                if(isBlack(w.getLeft()) && isBlack(w.getRight())){
                    if(w != NIL) w.setRed(true);
                    x = x.getParent();
                } else{
                    if(isBlack(w.getLeft())){
                        w.getRight().setRed(false);
                        w.setRed(true);
                        rotateLeft(w);
                        w = x.getParent().getLeft();
                    }
                    w.setRed(x.getParent().isRed());
                    x.getParent().setRed(false);
                    w.getLeft().setRed(false);
                    rotateRight(x.getParent());
                    x= root;
                }
            }
        }
        x.setRed(false);
    }

    public static void main(String[] args) {
        
    }
    
}
