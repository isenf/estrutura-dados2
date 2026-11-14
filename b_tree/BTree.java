package b_tree;
import b_tree.Node.Entry;

public class BTree <Key extends Comparable<Key>, Value> {
    private final int t;
    private Node<Key, Value> root;
    private int size;

    public BTree(){
        this(2);
    }

    public BTree(int t){
        if (t<2)
            throw new IllegalArgumentException("t must be >=2");
        this.t = t;
        this.root = null;
        this.size = 0;
    }

    public int size(){
        return this.size;
    }

    public boolean isEmpty(){
        return this.size == 0;
    }

    public int getT(){
        return this.t;
    }

    public int height(){
        if(root == null) return -1;

        int h = 0;
        Node<Key, Value> cur = root;
        while (!cur.leaf) {
            h++;
            cur = cur.children[0];
        }
        
        return h;
    }

    // search methods
    public Value search(Key key){
        Entry<Key, Value> e = root == null?null: search(root, key);
        return e == null ? null : e.value;
    }

    public boolean contains(Key key){
        return search(key) != null;
    }

    private Entry<Key, Value> search(Node<Key, Value> node, Key key){
        int i = 0;
        while (i<node.n && key.compareTo(node.entries[i].key) > 0) i++;
        if(i < node.n && key.compareTo(node.entries[i].key) == 0) return node.entries[i];
        if(node.leaf) return null;
        return search(node.children[i], key);
    }

}
