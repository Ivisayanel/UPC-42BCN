/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: isanchez <isanchez@42barcelona.com>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/24 09:24:23 by isanchez          #+#    #+#             */
/*   Updated: 2023/03/23 17:18:27 by isanchez         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	static char		*substr;
	unsigned int	size_s;
	size_t			i;
	size_t			k;

	size_s = ft_strlen(s);
	substr = malloc((len + 1) * sizeof(char));
	if (size_s <= start)
	{
		substr[0] = 0;
		return (substr);
	}
	if (substr == 0)
		return (NULL);
	i = (size_t) start;
	k = 0;
	while (s[i] && k < len)
	{
		substr[k] = s[i];
		i++;
		k++;
	}
	substr[i - start] = 0;
	return ((char *) substr);
}
