package red_black;

public class Node<Key, Value> {
    private Key key;
    private Value value;
    private boolean red;
    private Node<Key, Value> parent;
    private Node<Key, Value> left;
    private Node<Key, Value> right;

    public Node(Key key, Value value) {
        this.key = key;
        this.value = value;
        this.red = true;
        this.parent = null;
        this.left = null;
        this.right = null;
    }

    public Node() {
        this.key = null;
        this.value = null;
        this.red = true;
        this.parent = null;
        this.left = null;
        this.right = null;
    }

    public void setKey(Key newKey){
        this.key = newKey;
    }

    public void setValue(Value newValue){
        this.value = newValue;
    }

    public void setParent(Node<Key, Value> parent){
        this.parent = parent;
    }

    public void setLeft(Node<Key, Value> left){
        this.left = left;
    }

    public void setRight(Node<Key, Value> right){
        this.right = right;
    }

    public void setRed(boolean red){
        this.red = red;
    }

    public Key getKey(){
        return this.key;
    }

    public Value getValue(){
        return this.value;
    }

    public boolean isRed(){
        return this.red;
    }

    public String getColorString(){
        return isRed() ? "red" : "black";
    }

    public Node<Key, Value> getParent(){
        return this.parent;
    }

    public Node<Key, Value> getLeft(){
        return this.left;
    }

    public Node<Key, Value> getRight(){
        return this.right;
    }

    public static void main(String[] args) {
        
    }
}