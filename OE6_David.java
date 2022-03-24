
class Node {
    int key;
    Node leftST, rightST;

    public Node(int data) {
        key = data;
        leftST = rightST = null;
    }
}

public class OE6_David {
    Node root;

    //in-order traversal
    public void InOrder(Node node) {
        if(node != null) {
            InOrder(node.leftST);
            System.out.print(" " + node.key);
            InOrder(node.rightST);
        }
    }
    //pre-order traversal
    public void PreOrder(Node node) {
        if(node != null) {
            System.out.print(" " + node.key);
            PreOrder(node.leftST);
            PreOrder(node.rightST);
        }
    }
    //post-order traversal
    public void PostOrder(Node node) {
        if(node != null) {
            PostOrder(node.leftST);
            PostOrder(node.rightST);
            System.out.print(" " + node.key);
        }
    }

    public static void main(String[] args) {
        //Instance of the tree
        OE6_David myTree = new OE6_David();

        //Create Nodes
        myTree.root = new Node(10);
        myTree.root.leftST = new Node(20);
        myTree.root.rightST = new Node(30);
        myTree.root.leftST.leftST = new Node(40);
        myTree.root.leftST.rightST = new Node(50);
        myTree.root.rightST.leftST = new Node(60);
        myTree.root.rightST.rightST = new Node(70);

        System.out.println("\nIn-Order Tree Traversal:");
        myTree.InOrder(myTree.root);

        System.out.println("\nPre-Order Tree Traversal:");
        myTree.PreOrder(myTree.root);
 
        System.out.println("\nPost-Order Tree Traversal:");
        myTree.PostOrder(myTree.root);
     }
}