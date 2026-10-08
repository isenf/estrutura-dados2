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


    public boolean isEmpty(){
        return this.size == 0;
    }

    public void insert(Key key, Value value){
        this.root = insert(this.root, key, value);
    }


    public Value search(Key key){
        Node<Key, Value> n = search(root, key);
        return n == null ? null : n.getValue();
    }


    public void delete(Key key){
        if(!contains(key)) return;
        root = delete(root, key);
        size--;
    }


    public boolean contains(Key key){
        return search(root, key) != null;
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


    protected Node<Key, Value> search(Node<Key, Value> node, Key key){
        while(node != null){
            int comp = key.compareTo(node.getKey());
            
            if(comp < 0) node = node.getLeft();
            else if (comp > 0) node = node.getRight();
            else return node;
        }

        return null;
    }


    protected Node<Key, Value> delete(Node<Key, Value> node, Key key){
        if(node == null) return null;

        int comp = key.compareTo(node.getKey());

        if(comp < 0){
            node.setLeft(delete(node.getLeft(), key));
        } else if (comp > 0){
            node.setRight(delete(node.getRight(), key));
        } else{
            if(node.getLeft()==null) return node.getRight();
            if(node.getRight() == null) return node.getLeft();

            Node<Key, Value> successor = minNode(node.getRight());
            node.setKey(successor.getKey());
            node.setValue(successor.getValue());
            node.setRight(delete(node.getRight(), successor.getKey()));
        }

        updateHeight(node);
        return node;
    }


    protected Node<Key, Value> minNode(Node<Key, Value> node){
        while(node.getLeft() != null) node = node.getLeft();
        return node;
    }


    protected Node<Key, Value> maxNode(Node<Key, Value> node){
        while(node.getRight() != null) node = node.getRight();
        return node;
    }


    protected void updateHeight(Node<Key, Value> node){
        int lh = (node.getLeft() == null) ? -1: node.getLeft().getHeight();
        int rh = (node.getRight() == null) ? -1: node.getRight().getHeight();

        node.setHeight(1+Math.max(lh, rh));
    }


    public void preOrder(){
        preOrder(this.root);
    }


    protected void preOrder(Node<Key, Value> node){
        if(node == null) return;

        System.out.println(node.getKey() +" -> "+node.getValue());
        preOrder(node.getLeft());
        preOrder(node.getRight());
    }



    public static void main(String[] args) {
        BST<Integer, String> tree = new BST<>();

        tree.insert(50,"a50");
        tree.insert(60,"a60");
        tree.insert(10,"a10");
        tree.insert(30,"a30");
        tree.insert(20,"a20");
        tree.insert(80,"a80");
        tree.preOrder();
    }
}
