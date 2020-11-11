#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};

// Inserting nodes to test
struct node* insert( struct node* root, int data ) {
	if(root == NULL) {
        struct node* node = (struct node*)malloc(sizeof(struct node));
        node->data = data;
        node->left = NULL;
        node->right = NULL;
        return node;
	} else {
		struct node* cur;
		if(data <= root->data) {
            cur = insert(root->left, data);
            root->left = cur;
		} else {
            cur = insert(root->right, data);
            root->right = cur;
		}
		return root;
	}
}


int getHeight(struct node* root) {
  int left_count, right_count = 0;

  // if tree is empty
  if (root == NULL) {
    return -1;
  }

  // recursive alorithm
  left_count = getHeight(root->left);
  right_count = getHeight(root->right);

  if (left_count>=right_count){
    return (left_count+1);
  }
  else{
    return (right_count+1);
  }
  // a one liner
  // return 1 + findMax(getHeight(root->left), getHeight(root->right));
}


int main() {
    struct node* root = NULL;
    int t;
    int data;
    scanf("%d", &t);
    while(t-- > 0) {
        scanf("%d", &data);
        root = insert(root, data);
    }
	printf("%d",getHeight(root));
    return 0;
}
