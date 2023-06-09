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
	listint_t *node, *head = list;
	int i = 0, n = 0;

	if (list == NULL)
		return (0);
	while (list != NULL)
	{
		node = head;
		n = 0;
		printf("\n==== %d = %d ====\n", i, list->n);
		while (node != list && node && n < i)
		{
			printf("\n%d = %d\n", n, node->n);
			if (list == node && n != i)
				return (1);
			node = node->next;
			n++;
		}
		i++;
		list = list->next;
	}
	return (0);
}
