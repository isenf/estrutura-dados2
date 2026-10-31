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
    
}
