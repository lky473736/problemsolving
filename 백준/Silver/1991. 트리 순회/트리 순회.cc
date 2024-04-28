#include <iostream>
#include <cstdio>
#include <cstring>
#include <stdlib.h>
#include <map>

typedef struct Node {
    char ldata;
    char rdata;
} Node;

std::map<char, Node> nodemap;

void recu_inorder (char data) {
    if (data != '.') {
        recu_inorder(nodemap[data].ldata);
        printf("%c", data);
        recu_inorder(nodemap[data].rdata);
    }
    
    return;
}

void recu_preorder(char data) {
    if (data != '.') {
        printf("%c", data);
        recu_preorder(nodemap[data].ldata);
        recu_preorder(nodemap[data].rdata);
    }
}

void recu_postorder(char data) {
    if (data != '.') {
        recu_postorder(nodemap[data].ldata);
        recu_postorder(nodemap[data].rdata);
        printf("%c", data);
    }
}

int main() {
    char data;
    char ldata, rdata;
    char root;
    
    int N;
    scanf ("%d", &N);
    
    for (int i = 0; i < N; i++) {
        std::cin >> data >> ldata >> rdata;
        
        nodemap[data].ldata = ldata;
        nodemap[data].rdata = rdata;
        
        if (i == 0) {
            root = data;
        }
    }

    recu_preorder (root);
    printf ("\n");
    recu_inorder (root);
    printf ("\n");
    recu_postorder (root);

    return 0;
}
