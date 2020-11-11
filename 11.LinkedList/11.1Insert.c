/* For your reference:
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;;
*/
// Insert data at position 
SinglyLinkedListNode* insertNodeAtPosition(SinglyLinkedListNode* head, int data, int position) {
    // new node declaration
    struct SinglyLinkedListNode *newNode;
    newNode = malloc(sizeof(struct SinglyLinkedListNode));
    newNode->data = data;

    // to traverse the list
    struct SinglyLinkedListNode *curr = head;

    // if list is null, insert
    if (head == NULL){
        return newNode;
    }

    // traverse the list
    int count = 0;
    while (count < position -1){
        curr= curr->next;
        count ++;
    }

    //connect new node with next
    newNode->next = curr->next;
    // connect current node with new node
    curr->next = newNode;
    return head;
}
