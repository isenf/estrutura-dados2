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

    public static void main(String[] args) {
        
    }
    
}
