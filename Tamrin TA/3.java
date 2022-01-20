class GFG 
{ 
static class Node  
{ 
    int data; 
    Node next; 
}; 

static Node circular(Node head) 
{ 
    Node start = head; 
    while (head.next != null) 
        head = head.next; 
         
    head.next = start; 
    return start; 
} 
  
static Node push(Node head, int data) 
{ 
    Node newNode = new Node(); 
    newNode.data = data; 
    newNode.next = (head);  
    (head) = newNode; 
      
    return head; 
} 

static void displayList( Node node) 
{ 
    Node start = node; 
  
    while (node.next != start) 
    { 
        System.out.print(" "+ node.data); 
        node = node.next; 
    } 
       
    System.out.print(" " + node.data); 
} 