package b_tree;

public class Node<Key extends Comparable<Key>, Value> {
    int n; // number of keys stored
    Entry<Key, Value>[] entries;
    Node<Key, Value>[] children;
    boolean leaf;


    public Node(int t, boolean leaf){
        this.entries = new Entry[2*t -1];
        this.children = new Node[2*t];
        this.leaf = leaf;
        this.n = 0;
    }


    public static final class Entry <K, V>{
        public final K key;
        public V value;

        public Entry(K key, V value){
            this.key = key;
            this.value = value;
        }
    }
}
