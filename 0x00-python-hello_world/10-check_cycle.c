#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if singly-linked list has a cycle.
 * @list: linked list to be checked.
 *
 * Return: 0 if no cycle else 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *ease = list;
	listint_t *quick = list;

	/* Check if list is null or contains only 1 node */
	if (!list || !list->next)
		return (0);

	while (ease->next && quick->next && quick->next->next)
	{
		ease = ease->next;
		quick = quick->next->next;

		if (ease == quick)
			return (1);
	}

	return (0);
}
