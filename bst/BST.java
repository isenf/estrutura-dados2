package bst;

public class BST <Key extends Comparable<Key>, Value> {
    protected Node<Key, Value> root;
    protected int size;

    public BST(){
        this.root = null;
        this.size=0;
    }


    public int size(){
        return this.size;
    }



    public void insert(Key key, Value value){
        this.root = insert(this.root, key, value);
    }


    protected Node<Key, Value> insert(Node<Key, Value> node, Key key, Value value){
        if(node == null){
            size++;
            return new Node<>(key, value);
        }

        int comp = key.compareTo(node.getKey());
        if(comp < 0){
            node.setLeft(insert(node.getLeft(), key, value));
        } else if(comp >0){
            node.setRight(insert(node.getRight(), key, value));
        } else{
            node.setValue(value);
        }

        updateHeight(node);
        return  node;
    }


    protected void updateHeight(Node<Key, Value> node){
        int lh = (node.getLeft() == null) ? 0: node.getLeft().getHeight();
        int rh = (node.getLeft() == null) ? 0: node.getRight().getHeight();

        node.setHeight(1+Math.max(lh, rh));
    }


    public static void main(String[] args) {
        
    }
}
