/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: isanchez <isanchez@42barcelona.com>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/24 09:23:36 by isanchez          #+#    #+#             */
/*   Updated: 2023/03/23 16:22:03 by isanchez         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	char	*p;
	char	l;
	int		m;
	size_t	i;
	size_t	k;

	p = 0;
	l = c;
	m = 0;
	i = 0;
	while (s[i])
	{
		if (s[i] == l)
		{
			k = i;
			m = 1;
		}
		i++;
	}
	if (s[i] == l)
		return ((char *)(s + i));
	else if (m)
		return ((char *)(s + k));
	return (p);
}
