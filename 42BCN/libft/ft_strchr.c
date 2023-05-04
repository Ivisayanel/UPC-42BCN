/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: isanchez <isanchez@42barcelona.com>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/24 09:23:17 by isanchez          #+#    #+#             */
/*   Updated: 2023/03/23 17:17:08 by isanchez         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(const char *s, int c)
{
	char	*p;
	char	l;
	size_t	i;

	p = 0;
	l = c;
	i = 0;
	while (s[i] != l && s[i])
		i++;
	if (s[i] == l)
		return ((char *)(s + i));
	return (p);
}
