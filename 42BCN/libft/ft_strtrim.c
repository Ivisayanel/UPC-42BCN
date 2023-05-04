/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: isanchez <isanchez@42barcelona.com>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/24 09:23:38 by isanchez          #+#    #+#             */
/*   Updated: 2023/03/23 17:16:04 by isanchez         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t		i;
	size_t		k;
	static char	*trim;
	size_t		len;

	i = 0;
	k = 0;
	len = ft_strlen(s1);
	if (!s1 || !set)
		return (NULL);
	while (s1[i] && ft_strchr(set, s1[i]))
		i++;
	while (len > i && ft_strchr(set, s1[len - 1]))
		len--;
	trim = malloc((len - i) * sizeof(char) + 1);
	if (!trim)
		return (NULL);
	while (i < len)
	{
		trim[k] = s1[i];
		k++;
		i++;
	}
	trim[k] = 0;
	return (trim);
}
