#include "lists.h"
#include <stdlib.h>


/**
 * insert_node - inserts a node into a sorted linked list
 * @head: Pointer to the first node.
 * @number: Number to be inserted.
 *
 * Return: Pointer to new node, or NULL if it fails.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *n_node;

	n_node = malloc(sizeof(listint_t));
	if (!n_node)
		return (NULL);

	n_node->n = number;

	/* If list is empty or num to be inserted is less than the first number */
	if (*head == NULL || current->n >= number)
	{
		n_node->next = *head;
		*head = n_node;
		return (n_node);
	}

	/* If number to be inserted is within the range of the list */
	while (current->next)
	{
		if (current->n <= number && current->next->n >= number)
		{
			n_node->next = current->next;
			current->next = n_node;
			return (n_node);
		}
		current = current->next;
	}

	/* If number to be inserted is greater than the last number */
	if (!current->next)
	{
		n_node->next = current->next;
		current->next = n_node;
	}

	return (n_node);
}
