#include "lists.h"
/**
 * check_cycle - check_cycle
 * @list: list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node;

	while (list != NULL)
	{
		node = list->next;
		while (node != NULL)
		{
			if (list == node)
				return (1);
			node = node->next;
		}
		list = list->next;
	}

	return (0);
}
