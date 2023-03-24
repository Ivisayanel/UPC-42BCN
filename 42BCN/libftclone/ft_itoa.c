/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: isanchez <isanchez@42barcelona.com>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/26 10:14:20 by isanchez          #+#    #+#             */
/*   Updated: 2023/03/21 17:13:00 by isanchez         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static char	*make_str(char *str, unsigned int num, size_t i, size_t i_len)
{
	size_t	j;

	if (str == NULL)
		return (NULL);
	str[i] = 0;
	j = i;
	while (j > (i - i_len))
	{
		str[j - 1] = (num % 10) + 48;
		num /= 10;
		j--;
	}
	return (str);
}

static size_t	int_len(unsigned int num)
{
	unsigned int	num2;
	unsigned int	num3;
	unsigned int	dec;
	static size_t	i = 0;

	num2 = 0;
	if (num == 0)
		return (1);
	num3 = num;
	dec = 1;
	if (num2 < num)
	{
		num2 = (num2 + (num3 % 10) * dec);
		num3 /= 10;
		i++;
	}
	while (num2 < num)
	{
		dec *= 10;
		num2 = (num2 + (num3 % 10) * dec);
		num3 /= 10;
		i++;
	}
	return (i);
}

char	*num_expected(int num)
{
	static char		*s;
	int				i;
	unsigned int	u_num;

	s = malloc(12 * sizeof(char));
	s[0] = '-';
	s[11] = 0;
	i = 10;
	u_num = (-1) * num;
	while (i > 0)
	{
		s[i] = u_num % 10 + 48;
		u_num /= 10;
		i--;
	}
	return (s);
}

char	*ft_itoa(int n)
{
	unsigned int	num;
	char			*str;
	static int		sign = 1;
	size_t			i;

	if (n == -2147483648)
		return (ft_strdup("-2147483648"));
	if (n < 0)
		sign = -1;
	num = n * sign;
	i = int_len(num);
	if (sign == -1)
	{
		str = malloc((i + 2) * sizeof(char));
		if (str == NULL)
			return (NULL);
		str[0] = '-';
		make_str(str, num, i + 1, i);
	}
	else
	{
		str = malloc((i + 1) * sizeof(char));
		make_str(str, num, i, i);
	}
	return (str);
}
