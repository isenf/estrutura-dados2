package avl;

public class AVL <Key extends Comparable<Key>, Value> {
    protected Node<Key, Value> root;
    protected int size;

    public AVL(){
        this.root=null;
        this.size = 0;
    }

    public int size(){
        return this.size;
    }

    public boolean isEmpty(){
        return this.size == 0;
    }

    public int height(){
        return root == null ? -1: root.getHeight();
    }

    public Key min(){
        return root == null? null : minNode(root).getKey();
    }

    public Key max(){
        return root == null? null : maxNode(root).getKey();
    }

    public boolean contains(Key key){
        return search(root, key) != null;
    }

    public Node<Key, Value> maxNode(){
        return maxNode(root);
    }

    public void inOrder(){
        inOrder(root);
    }

    public void preOrder(){
        preOrder(root);
    }

    public void postOrder(){
        postOrder(root);
    }

    // helpers

    protected Node<Key, Value> search(Node<Key, Value> node, Key key){
        while(node != null){
            int comp = key.compareTo(node.getKey());

            if(comp < 0)
                node = node.getLeft();
            else if(comp > 0)
                node = node.getRight();
            else
                return node;
        }

        return null;
    }

    protected Node<Key, Value> minNode(Node<Key, Value> node){
        while (node.getLeft() != null) {
            node = node.getLeft();
        }

        return node;
    }

    protected Node<Key, Value> maxNode(Node<Key, Value> node){
        while(node.getRight() != null){
            node = node.getRight();
        }

        return node;
    }

    protected void inOrder(Node<Key,Value> node){
        if(node == null) return;

        inOrder(node.getLeft());
        System.out.println(node.getKey() +" -> "+node.getValue());
        inOrder(node.getRight());
    }

    protected void preOrder(Node<Key, Value> node){
        if(node == null) return;

        System.out.println(node.getKey() +" -> "+node.getValue());
        preOrder(node.getLeft());
        preOrder(node.getRight());
    }

    protected void postOrder(Node<Key, Value> node){
        if(node == null) return;

        postOrder(node.getLeft());
        postOrder(node.getRight());
        System.out.println(node.getKey() +" -> "+node.getValue());
    }

    public static void main(String[] args) {
        
    }
}
