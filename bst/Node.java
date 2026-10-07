package bst;

public class Node<Key, Value> {
    private Key key;
    private Value value;
    private int height;
    private Node<Key, Value> left;
    private Node<Key, Value> right;

    public Node(Key key, Value value) {
        this.key = key;
        this.value = value;
        this.height = 0;
        this.left = null;
        this.right = null;
    }

    public Node() {
        this.key = null;
        this.value = null;
        this.left = null;
        this.right = null;
    }

    public void setKey(Key newKey){
        this.key = newKey;
    }

    public void setValue(Value newValue){
        this.value = newValue;
    }

    public void setHeight(int height){
        this.height = height;
    }

    public void setLeft(Node<Key, Value> left){
        this.left = left;
    }

    public void setRight(Node<Key, Value> right){
        this.right = right;
    }

    public Key getKey(){
        return this.key;
    }

    public Value getValue(){
        return this.value;
    }

    public int getHeight(){
        return this.height;
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