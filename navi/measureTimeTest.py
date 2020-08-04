#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# measureTimeTest.py

import time

def measureTimeError_a(setting_time):
    start = time.time()
    time.sleep(setting_time)
    error = (time.time() - start) - setting_time
    return error

def measureTimeError_b(setting_time):
    start = time.perf_counter()
    time.sleep(setting_time)
    error = (time.perf_counter() - start) - setting_time
    return error

def measureTimeError_c(setting_time):
    start = time.process_time()
    time.sleep(setting_time)
    end = time.process_time()
    elapsed_time = end - start
    error = elapsed_time - setting_time
    return error

def test(num_trial):
    for i in range(num_trial):
        print("a: ", measureTimeError_a(5.0), "[sec]")
        print("b: ", measureTimeError_b(5.0), "[sec]")
        print("c: ", measureTimeError_b(5.0), "[sec]")
    return

def testCalcAverage(num_trial):
    sum_a = 0.0
    sum_b = 0.0
    sum_c = 0.0
    for i in range(num_trial):
        sum_a = sum_a + measureTimeError_a(1.0)
        sum_b = sum_b + measureTimeError_b(1.0)
        sum_c = sum_c + measureTimeError_c(1.0)
        print(i)
    ave_a = sum_a / num_trial
    ave_b = sum_b / num_trial
    ave_c = sum_c / num_trial
    print("a: ", ave_a, "b: ", ave_b, "c: ", ave_c)

if __name__ == "__main__":
    testCalcAverage(10)
