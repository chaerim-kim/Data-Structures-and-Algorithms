
static DoublyLinkedListNode sortedInsert(DoublyLinkedListNode head, int data) {
// create new node
DoublyLinkedListNode newNode = new DoublyLinkedListNode(data);

// if the list is empty
if (head == null){
    return newNode;
}

// insert at the front of the list
else if (head.data > newNode.data){
  newNode.next = head;
  head.prev = newNode;
  return newNode;
}

else{
  DoublyLinkedListNode curr = head;
  while (curr.next != null){
    // if next is not bigger, continue
    if (curr.next.data < newNode.data){
      curr = curr.next;
    }
    else{
      // insert in the middle and connect
      newNode.next = curr.next;
      curr.next.prev = newNode;
      curr.next = newNode;
      newNode.prev = curr;
      return head;
    }
  }
    // insert at tail
    curr.next = newNode;
    newNode.next = null;
    newNode.prev = curr;
  }
  return head;
}
