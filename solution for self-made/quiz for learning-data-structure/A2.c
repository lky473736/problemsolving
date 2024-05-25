#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct list {
    int data; // data field
    struct list *link; // link field
};

int main()
{
    int arr_data[3] = {100, 200, 300};
    struct list *head, *prev;
    
    for (int i = 0; i < 3; i++) {
        struct list *linked_list = (struct list *) malloc (sizeof(struct list));
        linked_list->data = arr_data[i];
        
        if (i == 0) {
            head = linked_list;
        }
        
        else {
            prev->link = linked_list;
            
            if (i == 3 - 1) { 
                linked_list->link = NULL;
            }
        }
        
        prev = linked_list;
    }
    
    int counting = 0;
    
    while (true) {
        printf ("%p | number %d data of linked list : %d\n", head, ++counting, head->data);

        if (head->link == NULL) {
            printf ("detected NULL\n");
            free(head->link);
            break;
        }
        
        struct list *free_address = head;
        head = head->link;
        free(free_address);
    }
    
    return 0;
}
