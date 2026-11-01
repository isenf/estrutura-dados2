package red_black;


public class RedBlack <Key extends Comparable<Key>, Value> {
    private final Node<Key, Value> NIL;
    protected Node<Key, Value> root;
    protected int size;

    public RedBlack(){
        NIL = new Node<>();
        NIL.setRed(false);
        NIL.setParent(null);;
        NIL.setLeft(null);;
        NIL.setRight(null);;
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

    public static void main(String[] args) {
        
    }
    
}
