

/**
 * check_cycle - check_cycle
 * @list: list
 * @node: node to be checked
 * @i: index
 *
 * Return: 1 if there is loop, 0 if not
 */
int check_cycle(listint_t *list)
{

	int idx = 0, occurrence = 0;
  listint_t *ptr_lst;
	/*printf("%i" , i);*/
	while (idx != i + 1)
	{
		/*printf("   [%p] %i : %i (occ : %i)\n", (void *)head, idx, i, occurrence);*/
		if (head == node)
			occurrence++;
		head = head->next;
		idx++;
	}
	if (occurrence > 1)
	{
		return (1);
	}
	return (0);
}
