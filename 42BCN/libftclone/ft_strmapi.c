/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: isanchez <isanchez@student.42barcel>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/30 08:48:37 by isanchez          #+#    #+#             */
/*   Updated: 2023/01/30 09:07:51 by isanchez         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char	*new_str;
	size_t	i;
	int		len;

	len = ft_strlen(s);
	new_str = malloc((len + 1) * sizeof(char));
	if (new_str == NULL)
		return (NULL);
	new_str[len] = 0;
	i = 0;
	while (s[i])
	{
		new_str[i] = f(i, s[i]);
		i++;
	}
	return (new_str);
}
