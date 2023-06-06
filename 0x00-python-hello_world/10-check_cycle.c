#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check_cycle
 * @list: list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node;

	if (list == NULL)
		return (0);
	while (list != NULL)
	{
		printf("\n(l= %d)\n", list->n);
		node = list->next;
		while (node != NULL)
		{
			printf("(n= %d)\n", node->n);
			if (list == node)
				return (1);
			node = node->next;
		}
		list = list->next;
	}
	return (0);
}
