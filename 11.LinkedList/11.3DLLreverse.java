static DoublyLinkedListNode reverse(DoublyLinkedListNode head){

    DoublyLinkedListNode curr = head;
    DoublyLinkedListNode temp = null;

    while (curr != null){
        // reverse the pointers
        temp = curr.prev;
        // this case curr.next == null
        curr.prev = curr.next;
        curr.next = temp;
        curr = curr.prev;
    }

    if (temp != null){
        // change the head
        head = temp.prev;
    }
    return head;
}
