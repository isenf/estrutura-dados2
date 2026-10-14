package avl;

public class AVL <Key, Value> {
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


    public static void main(String[] args) {
        
    }
}
