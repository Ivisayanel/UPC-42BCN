/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: isanchez <isanchez@42barcelona.com>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/24 09:23:33 by isanchez          #+#    #+#             */
/*   Updated: 2023/03/23 16:21:11 by isanchez         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *haystack, const char *needle, size_t len)
{
	size_t	i;
	size_t	k;
	char	*a;

	a = 0;
	if (!(*needle))
		return ((char *) haystack);
	i = 0;
	k = 0;
	while (haystack[i] && needle[k] && i < len)
	{
		if (haystack[i] == needle[k])
			k++;
		else
			k = 0;
		i++;
	}
	if (!(needle[k]))
		return ((char *)(haystack + i - k));
	else
		return (a);
}
