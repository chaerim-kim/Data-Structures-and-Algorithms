// We assume that there are no duplicates.
// The  value of every node in a node's left subtree is less than the data value of that node.
// The  value of every node in a node's right subtree is greater than the data value of that node.

bool checkBST(Node* root) {
  // initialize a min and max variable
  int l=-1000000,r=1000000;
  return checkBSTutil(root, l, r);
}

bool checkBSTutil(Node* n, int min, int max){
  // if tree is null, it is BST
  if (n == NULL) return 1;
  // if its out of range, return false
  if (n->data <= min || n->data >= max){
    return 0;
  }
  // when going left, the left nodes always have to be smaller than the root hence the max it could be is the root node
  // for the right, the smallest it could be is the data itself hence n.data is min
  if (!checkBSTutil(n->left, min, n->data) || !checkBSTutil(n->right, n->data, max)){
    return 0;
  }
  return 1;
}
