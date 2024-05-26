/*

        4
       / \
      1   5
     / \   \
   -1   3   10
       /
      2


preorder : 4 1 -1 3 2 5 10
inorder : -1 1 2 3 4 5 10
postorder : -1 2 3 1 10 5 4
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* lchild;
    struct Node* rchild;
} Node;

Node* init_node (int data) {
    Node* node = (Node*)malloc(sizeof(Node));
    
    node->data = data;
    node->lchild = NULL;
    node->rchild = NULL;
    
    return node;
}

void insert_node (Node** current_node, int data) {
    if (*current_node == NULL) {
        *current_node = init_node(data);
        return;
    }
    
    if (data < (*current_node)->data) {
        insert_node(&(*current_node)->lchild, data);
    } 
    
    else {
        insert_node(&(*current_node)->rchild, data);
    }
}

void recu_inorder (Node* current_node) {
    if (current_node != NULL) {
        recu_inorder(current_node->lchild);
        printf("%d ", current_node->data);
        recu_inorder(current_node->rchild);
    }
}

int main() {
    int arr[] = {4, 1, 3, 2, 5, 10, -1};
    Node* root = NULL;
    
    for (int i = 0; i < 7; i++) {
        insert_node(&root, arr[i]);
    }

    recu_inorder (root);

    return 0;
}
