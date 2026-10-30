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

    public Value search(Key key){
        Node<Key, Value> n = search(root, key);
        return n == null ? null : n.getValue();
    }

    public void insert(Key key, Value val){
        root = insert(root, key, val);
    }

    public Node<Key, Value> maxNode(){
        return root == null ? null : maxNode(root);
    }

    public  Node<Key, Value> minNode(){
        return root == null ? null : minNode(root);
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

    protected Node<Key, Value> insert(Node<Key, Value> node, Key key, Value val){
        if(node == null){
            this.size++;
            return new Node<>(key, val);
        }

        int comp = key.compareTo(node.getKey());
        if(comp < 0){
            node.setLeft(insert(node.getLeft(), key, val));
        } else if(comp > 0){
            node.setRight(insert(node.getRight(), key, val));
        } else{
            node.setValue(val);
        }

        return rebalance(node);
    }

    protected int balanceFactor(Node<Key, Value> node){
        int lh = node.getLeft() == null ? -1 : node.getLeft().getHeight();
        int rh = node.getRight() == null ? -1 : node.getRight().getHeight();

        return lh - rh;
    }

    protected Node<Key, Value> rebalance(Node<Key, Value> node){
        updateHeight(node);
        int bf = balanceFactor(node);

        if(bf > 1){
            if(balanceFactor(node.getLeft()) < 0){  // left-right case
                node.setLeft(rotateLeft(node.getLeft()));
            }
            return rotateRight(node);
        }

        if(bf < -1){
            if(balanceFactor(node.getRight()) > 0){ // right-left case
                node.setRight(rotateRight(node.getRight()));
            }
            return rotateLeft(node);
        }

        return node; // already balanced case
    }

    
    protected Node<Key, Value> rotateRight(Node<Key, Value> n){
        Node<Key, Value> x = n.getLeft();
        Node<Key, Value> y = x.getRight();

        x.setRight(n);
        n.setLeft(y);
        updateHeight(n);
        updateHeight(x);
        return x;
    }

    protected Node<Key, Value> rotateLeft(Node<Key, Value> n){
        Node<Key, Value> x = n.getRight();
        Node<Key, Value> y = x.getLeft();

        x.setLeft(n);
        n.setRight(y);
        updateHeight(n);
        updateHeight(x);
        return x;
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

    protected void updateHeight(Node<Key, Value> node){
        int lh = node.getLeft() == null ? -1 : node.getLeft().getHeight();
        int rh = node.getRight() == null ? -1 : node.getRight().getHeight();
        node.setHeight(1 + Math.max(lh, rh));
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
