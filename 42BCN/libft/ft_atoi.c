/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: isanchez <isanchez@42barcelona.com>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/24 09:22:46 by isanchez          #+#    #+#             */
/*   Updated: 2023/01/28 08:21:01 by isanchez         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_atoi(const char *str)
{
	size_t			i;
	int				sign;
	unsigned int	k;

	sign = 1;
	k = 0;
	i = 0;
	while (((str[i] >= 9 && str[i] <= 13) || (str[i] == 32)) && str[i])
		i++;
	if (str[i] == '-')
		sign = -1;
	if (str[i] == '+' || str[i] == '-')
		i++;
	while (str[i] >= 48 && str[i] <= 57 && str[i])
	{
		k += (str[i] - 48);
		if (str[i + 1] >= 48 && str[i + 1] <= 57 && str[i + 1])
			k *= 10;
		i++;
	}
	return ((int) k * sign);
}
