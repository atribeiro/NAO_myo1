from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "192.168.8.1", 9559) #192.168.8.1



startCommand = 1

triggered = False
while startCommand == 1:
    #tts.say ("I am open and reading his heart and blood oxygen level measurements")
    myo_file_Tap = open('C:/Users/Anabela/Documents/GitHub/NAO_myo1/examples/acceleration.txt', 'r')
    myo_file_line= myo_file_Tap.readlines()
    file_length = len(myo_file_line)
    file_length -= 1

    #print(a)
    line = myo_file_line[file_length].strip()[1:-1]
    acceleration = line.split(",")

    acceleration_x = float(acceleration[0])
    acceleration_y = float(acceleration[1])
    acceleration_z = float(acceleration[2])

    #acceleration_x = -0.603

    if (acceleration_x < - 0.50) and not triggered:

        memoryEvent = ALProxy("ALMemory", "192.168.8.1", 9559) #192.168.8.1
        memoryEvent.raiseMicroEvent("RotatePatient", 2)
        triggered = True
        print "sent event"
    else:
        print("It is okay")
        triggered = False


    #if stopProgram == 1:
    #    print("I am closing the programming")
    #    break



