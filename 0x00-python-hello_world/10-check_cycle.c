#include "lists.h"

/**
 *check_cycle - checks whether a s-linked list is circular
 *@list: the list to check
 *Return: 0 for no cycle and 1 for a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *end = list;
	listint_t *start = list;

	if (!list)
		return (0);
	while (start && end && end->next)
	{
		start = start->next;
		end = end->next->next;
		if (start == end)
			return (1);
	}

	return (0);
}
