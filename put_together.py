while True:
    if api.getSpinIsColorFound([100, 0, 0], 'QLQ'):
        api.spinByMetric(-90, 'degrees', 'QLQ', 100)
        api.wait(5)
    elif api.getSpinIsColorFound([0, 0, 100], 'QLQ'):
        api.spinByMetric(90, 'degrees', 'QLQ', 100)
        api.wait(5)
    elif api.spinObstacleDetected(10, 'QLQ'):
        api.setSpinSpeed(0, 0, 'QLQ')
        api.wait(1)
        break
    api.setSpinSpeed(-50, 50, 'QLQ')