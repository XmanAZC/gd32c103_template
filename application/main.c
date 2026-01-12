/*
 * Copyright (c) 2006-2022, RT-Thread Development Team
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * Change Logs:
 * Date           Author       Notes
 * 2021-08-20     BruceOu      first implementation
 */

#include <stdio.h>
#include <rtthread.h>
#include <rtdevice.h>
#include <board.h>

// #define LED0 GET_PIN(B, 7)

int main(void)
{
    // rt_pin_mode(LED0, PIN_MODE_OUTPUT);
    for (;;)
    {
        // rt_pin_write(LED0, !(rt_pin_read(LED0)));
        rt_thread_mdelay(100);
    }

    return RT_EOK;
}
