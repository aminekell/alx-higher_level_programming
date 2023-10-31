#include "lists.h"
int check_cycle(listint_t *list)
{
    listint_t *slow_ptr = list;
    listint_t *fast_ptr = list;

    while (slow_ptr != NULL && fast_ptr != NULL && fast_ptr->next != NULL)
    {
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;

        if (slow_ptr == fast_ptr)
        {
            return (1);
        }
    }

    return (0);
}

