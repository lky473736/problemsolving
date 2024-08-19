#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct node {
    int data;
    struct node* left;
    struct node* right;
};

int level_min[10001];
int level_max[10001];
int number = 1;

struct node* create_node(int data) {
    struct node* new_node = (struct node*) malloc (sizeof(struct node));
    
    new_node->data = data;
    new_node->left = NULL;
    new_node->right = NULL;
    
    return new_node;
}

void inorder(struct node* current, int level) {
    if (current == NULL) {
        return;
    }

    inorder(current->left, level + 1); // 왼쪽
    
    if (level_min[level] == 0 || level_min[level] > number) {
        level_min[level] = number;
    }
    
    if (level_max[level] == 0 || level_max[level] < number) {
        level_max[level] = number;
    }
    
    number++;
    
    inorder(current->right, level + 1); // 오른쪽
}

int main() {
    int num_nodes;
    scanf("%d", &num_nodes);

    struct node* nodes[10001];
    int have_bumo[10001];
    
    for (int i = 1; i <= num_nodes; i++) {
        nodes[i] = create_node(i); // 노드 만들기
    }

    for (int i = 0; i < num_nodes; i++) {
        int parent, left, right;
        scanf("%d %d %d", &parent, &left, &right); // 트리 만들기

        if (left != -1) {
            nodes[parent]->left = nodes[left];
            have_bumo[left] = 1;
        }
        
        if (right != -1) {
            nodes[parent]->right = nodes[right];
            have_bumo[right] = 1;
        }
    }

    struct node* root;
    for (int i = 1; i <= num_nodes; i++) {
        if (have_bumo[i] == false) { // 부모가 없으면 root다
            root = nodes[i];
            break;
        }
    }

    inorder(root, 1);

    int max_width = 0;
    int max_level = 0;
    
    for (int i = 1; i <= num_nodes; i++) { 
        int width = level_max[i] - level_min[i] + 1; // 가장 큰거 가장 작은거 빼기
        if (width > max_width) {
            max_width = width;
            max_level = i;
        }
    }
    
    printf("%d %d\n", max_level, max_width);
    return 0;
}

