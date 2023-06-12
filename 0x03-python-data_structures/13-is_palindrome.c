#include "lists.h"
#include <stdlib.h>
#include <stdbool.h>

int linked_list_length(listint_t **head);
int check_palindrome_bruteforce(listint_t **head);
int palindrome_reverse_half(listint_t **head);
listint_t *reverse(listint_t *start);

/**
 * is_palindrome - checks if  singly-linked list is a palindrome
 * @head: Pointer to head of list.
 *
 * Return: 0 if its not a palindrome or 1 if it is.
 */

int is_palindrome(listint_t **head)
{
    
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    
    if ((*head)->next->next == NULL)
        return ((*head)->n == (*head)->next->n ? 1 : 0);

    
    if ((*head)->next->next->next == NULL)
        return ((*head)->n == (*head)->next->next->n ? 1 : 0);

   
    return (palindrome_reverse_half(head));
}

/**
 * palindrome_reverse_half - checks if a singly-link list is a palindrome
 * @head: Pointer to head of list.
 *
 * This algorithm uses 2 pointers to track the middle of the list,
 * then reversing the second half and then comparing the respective elements.
 * It has a time complexity of 0(n) since the list is only traversed once.
 *
 * Return: 0 if its not a palindrome or 1 if it is.
 */

int palindrome_reverse_half(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;

    while (fast->next && fast->next->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    slow->next = reverse(slow->next);
    slow = slow->next;
    fast = *head;

    while (slow)
    {
        if (fast->n != slow->n)
            return (false);
        slow = slow->next;
        fast = fast->next;
    }

    return (true);
}

/**
 * check_palindrome_bruteforce - checks if a singly-linked list is a palindrome
 * @head: Pointer to head of list.
 *
 * This algorithm gets the length of the list, then allocates an array
 * of integers where the numbers from the list are copied to.
 *
 * Return: 0 if its not a palindrome or 1 if it is.
 */

int check_palindrome_bruteforce(listint_t **head)
{
    int x, list_len, left_idx, right_idx;
    int *numbers;
    listint_t *curr = *head;

    list_len = linked_list_length(head);

    
    numbers = malloc(sizeof(int) * list_len);
    if (!numbers)
        return (false);

    
    curr = *head;
    for (x = 0; x < list_len; x++, curr = curr->next)
        numbers[x] = curr->n;

    if ((list_len & 1) == 0)
    { 
        right_idx = list_len / 2;
        left_idx = right_idx - 1;
    }
    else if ((list_len & 1) == 1)
    { 
        right_idx = (list_len / 2) + 1;
        left_idx = (list_len / 2) - 1;
    }
    for (; left_idx >= 0; left_idx--, right_idx++)
        if (numbers[left_idx] != numbers[right_idx])
        {
            free(numbers);
            return (false);
        }

    free(numbers);
    return (true);
}

/**
 * linked_list_length - returns the length of a linked list
 * @head: Pointer to head of list.
 *
 * Return: Integer, the length of the list.
 */

int linked_list_length(listint_t **head)
{
    listint_t *curr = *head;
    int list_len = 1;

    while (curr->next)
    { 
        list_len++;
        curr = curr->next;
    }

    return (list_len);
}

/**
 * reverse - reverses a linked-list starting from a specified node
 * @start: Node to start reversing from.
 *
 * Return: Pointer to the first node after list has been reversed.
 */

listint_t *reverse(listint_t *start)
{
    listint_t *next = NULL;
    listint_t *prev = NULL;

    while (start)
    {
        next = start->next;
        start->next = prev;
        prev = start;
        start = next;
    }

    start = prev;
    return (start);
}
