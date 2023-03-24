/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: isanchez <isanchez@42barcelona.com>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/23 14:13:15 by isanchez          #+#    #+#             */
/*   Updated: 2023/03/21 17:31:59 by isanchez         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t count, size_t size)
{
	static char	*p;
	size_t		i;

	p = malloc(count * size);
	i = 0;
	while (i < count * size && p != 0)
	{
		p[i] = 0;
		i++;
	}
	return ((void *) p);
}
