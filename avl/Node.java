package red_black;

public class Node<Key, Value> {
    private Key key;
    private Value value;
    private int height;
    private int color;  // o -> red; 1 -> black.
    private Node<Key, Value> left;
    private Node<Key, Value> right;

    public Node(Key key, Value value) {
        this.key = key;
        this.value = value;
        this.height = 0;
        this.color = 0;
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

    public void setColor(int color){
        if(color != 0 || color != 1){
            throw new IllegalArgumentException("color must be 0 or 1");
        }

        this.color = color;
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

    public int getColor(){
        return this.color;
    }

    public String getColorString(){
        return this.color == 0 ? "red" : "black";
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