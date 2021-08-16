    from machine import Pin
    from machine import ADC
    from machine import DAC
    from math import log
    import utils_constants as constants

    import machine
    import utime

    # adc_V_lookup=open(adc_V_lookup.txt,"r")
    adc_V_lookup = [0.01235294, 0.009264706, 0.01852941, 0.02779412, 0.03705883, 0.04014706, 0.0432353, 0.04632353, 0.04941177, 0.05352942, 0.05764706, 0.06176471, 0.06485295, 0.06794118, 0.07102942, 0.07411765, 0.0782353, 0.08235294, 0.08647059, 0.09058825, 0.09470588, 0.09882354, 0.1019118, 0.105, 0.1080882, 0.1111765, 0.1152941, 0.1194118, 0.1235294, 0.1266177, 0.1297059, 0.1327941, 0.1358824, 0.1389706, 0.1420588, 0.1451471, 0.1482353, 0.1513235, 0.1544118, 0.1575, 0.1605882, 0.1636765, 0.1667647, 0.1698529, 0.1729412, 0.1770588, 0.1811765, 0.1852941, 0.1883824, 0.1914706, 0.1945588, 0.1976471, 0.2017647, 0.2058824, 0.21, 0.2130883, 0.2161765, 0.2192647, 0.222353, 0.2254412, 0.2285294, 0.2316177, 0.2347059, 0.2388236, 0.2429412, 0.2470588, 0.2501471, 0.2532353, 0.2563236, 0.2594118, 0.2635294, 0.2676471, 0.2717647, 0.274853, 0.2779412, 0.2810294, 0.2841177, 0.2872059, 0.2902942, 0.2933824, 0.2964706, 0.3005883, 0.3047059, 0.3088235, 0.3119118, 0.315, 0.3180882, 0.3211765, 0.3242647, 0.327353, 0.3304412, 0.3335294, 0.3376471, 0.3417647, 0.3458824, 0.3489706, 0.3520588, 0.3551471, 0.3582353, 0.362353, 0.3664706, 0.3705883, 0.3736765, 0.3767647, 0.379853, 0.3829412, 0.3860294, 0.3891177, 0.3922059, 0.3952941, 0.3983824, 0.4014706, 0.4045588, 0.4076471, 0.4117647, 0.4158824, 0.42, 0.4230883, 0.4261765, 0.4292647, 0.432353, 0.4354412, 0.4385294, 0.4416177, 0.4447059, 0.4477942, 0.4508824, 0.4539706, 0.4570589, 0.4601471, 0.4632353, 0.4663236, 0.4694118, 0.4725, 0.4755883, 0.4786765, 0.4817647, 0.484853, 0.4879412, 0.4910295, 0.4941177, 0.4972059, 0.5002942, 0.5033824, 0.5064706, 0.5105882, 0.5147059, 0.5188236, 0.5229412, 0.5270588, 0.5311765, 0.5342648, 0.537353, 0.5404412, 0.5435295, 0.547647, 0.5517647, 0.5558824, 0.5589706, 0.5620589, 0.5651471, 0.5682353, 0.5723529, 0.5764706, 0.5805883, 0.5830588, 0.5855294, 0.588, 0.5904706, 0.5929412, 0.5960294, 0.5991177, 0.6022058, 0.6052941, 0.6094118, 0.6135294, 0.6176471, 0.6207353, 0.6238235, 0.6269117, 0.63, 0.6341177, 0.6382353, 0.642353, 0.6454412, 0.6485294, 0.6516176, 0.6547059, 0.6588235, 0.6629412, 0.6670588, 0.6695294, 0.672, 0.6744706, 0.6769412, 0.6794118, 0.6835294, 0.6876471, 0.6917647, 0.6948529, 0.6979412, 0.7010294, 0.7041177, 0.7082353, 0.712353, 0.7164706, 0.7195588, 0.7226471, 0.7257353, 0.7288236, 0.7329412, 0.7370589, 0.7411765, 0.7436471, 0.7461177, 0.7485883, 0.7510588, 0.7535295, 0.757647, 0.7617648, 0.7658824, 0.77, 0.7741177, 0.7782353, 0.7813235, 0.7844118, 0.7875, 0.7905883, 0.7936765, 0.7967648, 0.7998529, 0.8029412, 0.8070589, 0.8111765, 0.8152942, 0.8183824, 0.8214706, 0.8245588, 0.8276471, 0.8307353, 0.8338236, 0.8369118, 0.8400001, 0.8461765, 0.852353, 0.8548235, 0.8572942, 0.8597647, 0.8622354, 0.8647059, 0.8677941, 0.8708824, 0.8739706, 0.8770589, 0.8801471, 0.8832354, 0.8863235, 0.8894118, 0.8925, 0.8955883, 0.8986765, 0.9017648, 0.904853, 0.9079412, 0.9110294, 0.9141177, 0.9172059, 0.9202942, 0.9233824, 0.9264707, 0.9305883, 0.9347058, 0.9388236, 0.9419118, 0.9450001, 0.9480883, 0.9511765, 0.9542647, 0.957353, 0.9604412, 0.9635295, 0.9676472, 0.9717647, 0.9758824, 0.9789706, 0.9820589, 0.9851471, 0.9882354, 0.9913236, 0.9944118, 0.9975, 1.000588, 1.003677, 1.006765, 1.009853, 1.012941, 1.016029, 1.019118, 1.022206, 1.025294, 1.029412, 1.033529, 1.037647, 1.040735, 1.043824, 1.046912, 1.05, 1.054118, 1.058235, 1.062353, 1.065441, 1.068529, 1.071618, 1.074706, 1.078824, 1.082941, 1.087059, 1.090147, 1.093235, 1.096324, 1.099412, 1.1025, 1.105588, 1.108677, 1.111765, 1.114853, 1.117941, 1.121029, 1.124118, 1.128235, 1.132353, 1.136471, 1.139559, 1.142647, 1.145735, 1.148824, 1.151912, 1.155, 1.158088, 1.161177, 1.165294, 1.169412, 1.17353, 1.175588, 1.177647, 1.179706, 1.181765, 1.183824, 1.185882, 1.19, 1.194118, 1.198235, 1.201324, 1.204412, 1.2075, 1.210588, 1.213676, 1.216765, 1.219853, 1.222941, 1.226029, 1.229118, 1.232206, 1.235294, 1.241471, 1.247647, 1.250735, 1.253824, 1.256912, 1.26, 1.263088, 1.266176, 1.269265, 1.272353, 1.275441, 1.278529, 1.281618, 1.284706, 1.288824, 1.292941, 1.297059, 1.300147, 1.303235, 1.306324, 1.309412, 1.311882, 1.314353, 1.316824, 1.319294, 1.321765, 1.324853, 1.327941, 1.331029, 1.334118, 1.337206, 1.340294, 1.343382, 1.346471, 1.350588, 1.354706, 1.358824, 1.361912, 1.365, 1.368088, 1.371176, 1.375294, 1.379412, 1.383529, 1.386, 1.388471, 1.390941, 1.393412, 1.395882, 1.4, 1.404118, 1.408235, 1.411324, 1.414412, 1.4175, 1.420588, 1.424706, 1.428824, 1.432941, 1.436029, 1.439118, 1.442206, 1.445294, 1.448382, 1.451471, 1.454559, 1.457647, 1.461765, 1.465882, 1.47, 1.473088, 1.476177, 1.479265, 1.482353, 1.486471, 1.490588, 1.494706, 1.497794, 1.500882, 1.503971, 1.507059, 1.510147, 1.513235, 1.516324, 1.519412, 1.5225, 1.525588, 1.528677, 1.531765, 1.535882, 1.54, 1.544118, 1.547206, 1.550294, 1.553382, 1.556471, 1.564706, 1.572941, 1.581177, 1.568824, 1.577059, 1.585294, 1.593529, 1.596618, 1.599706, 1.602794, 1.605882, 1.608971, 1.612059, 1.615147, 1.618235, 1.622353, 1.626471, 1.630588, 1.633677, 1.636765, 1.639853, 1.642941, 1.646029, 1.649118, 1.652206, 1.655294, 1.659412, 1.663529, 1.667647, 1.670735, 1.673824, 1.676912, 1.68, 1.684118, 1.688235, 1.692353, 1.695441, 1.698529, 1.701618, 1.704706, 1.707794, 1.710882, 1.713971, 1.717059, 1.721177, 1.725294, 1.729412, 1.7325, 1.735588, 1.738677, 1.741765, 1.744235, 1.746706, 1.749177, 1.751647, 1.754118, 1.758235, 1.762353, 1.766471, 1.769559, 1.772647, 1.775735, 1.778824, 1.781912, 1.785, 1.788088, 1.791177, 1.795294, 1.799412, 1.80353, 1.806618, 1.809706, 1.812794, 1.815882, 1.818971, 1.822059, 1.825147, 1.828235, 1.832353, 1.836471, 1.840588, 1.843677, 1.846765, 1.849853, 1.852941, 1.85603, 1.859118, 1.862206, 1.865294, 1.869412, 1.87353, 1.877647, 1.880735, 1.883824, 1.886912, 1.89, 1.893088, 1.896177, 1.899265, 1.902353, 1.908529, 1.914706, 1.917176, 1.919647, 1.922118, 1.924588, 1.927059, 1.931176, 1.935294, 1.939412, 1.9425, 1.945588, 1.948677, 1.951765, 1.955882, 1.96, 1.964118, 1.966588, 1.969059, 1.97153, 1.974, 1.976471, 1.979559, 1.982647, 1.985735, 1.988824, 1.992941, 1.997059, 2.001177, 2.004265, 2.007353, 2.010441, 2.01353, 2.017647, 2.021765, 2.025882, 2.028971, 2.032059, 2.035147, 2.038235, 2.041324, 2.044412, 2.0475, 2.050588, 2.053677, 2.056765, 2.059853, 2.062941, 2.067059, 2.071177, 2.075294, 2.078382, 2.081471, 2.084559, 2.087647, 2.090735, 2.093824, 2.096912, 2.1, 2.103088, 2.106177, 2.109265, 2.112353, 2.116471, 2.120588, 2.124706, 2.128824, 2.132941, 2.137059, 2.139529, 2.142, 2.144471, 2.146941, 2.149412, 2.153529, 2.157647, 2.161765, 2.164235, 2.166706, 2.169177, 2.171647, 2.174118, 2.178235, 2.182353, 2.186471, 2.188941, 2.191412, 2.193882, 2.196353, 2.198824, 2.201912, 2.205, 2.208088, 2.211177, 2.215294, 2.219412, 2.22353, 2.226618, 2.229706, 2.232794, 2.235883, 2.24, 2.244118, 2.248235, 2.250706, 2.253176, 2.255647, 2.258118, 2.260588, 2.264706, 2.268824, 2.272941, 2.27603, 2.279118, 2.282206, 2.285294, 2.289412, 2.29353, 2.297647, 2.300118, 2.302588, 2.305059, 2.307529, 2.31, 2.314118, 2.318235, 2.322353, 2.325441, 2.32853, 2.331618, 2.334706, 2.340883, 2.347059, 2.349118, 2.351177, 2.353235, 2.355294, 2.357353, 2.359412, 2.365588, 2.371765, 2.374853, 2.377941, 2.381029, 2.384118, 2.386588, 2.389059, 2.39153, 2.394, 2.396471, 2.400588, 2.404706, 2.408823, 2.411912, 2.415, 2.418088, 2.421176, 2.424265, 2.427353, 2.430441, 2.433529, 2.437647, 2.441765, 2.445882, 2.448353, 2.450824, 2.453294, 2.455765, 2.458235, 2.462353, 2.466471, 2.470588, 2.473676, 2.476765, 2.479853, 2.482941, 2.485412, 2.487882, 2.490353, 2.492824, 2.495294, 2.498382, 2.501471, 2.504559, 2.507647, 2.510118, 2.512588, 2.515059, 2.517529, 2.52, 2.524118, 2.528235, 2.532353, 2.534824, 2.537294, 2.539765, 2.542235, 2.544706, 2.548824, 2.552941, 2.557059, 2.55953, 2.562, 2.564471, 2.566941, 2.569412, 2.571471, 2.573529, 2.575588, 2.577647, 2.579706, 2.581765, 2.585882, 2.59, 2.594118, 2.596177, 2.598235, 2.600294, 2.602353, 2.604412, 2.606471, 2.610588, 2.614706, 2.618824, 2.621294, 2.623765, 2.626235, 2.628706, 2.631176, 2.633647, 2.636118, 2.638588, 2.641059, 2.643529, 2.646618, 2.649706, 2.652794, 2.655882, 2.658353, 2.660824, 2.663294, 2.665765, 2.668235, 2.671324, 2.674412, 2.6775, 2.680588, 2.682647, 2.684706, 2.686765, 2.688824, 2.690882, 2.692941, 2.695412, 2.697882, 2.700353, 2.702824, 2.705294, 2.709412, 2.71353, 2.717647, 2.719706, 2.721765, 2.723824, 2.725883, 2.727941, 2.73, 2.732471, 2.734941, 2.737412, 2.739882, 2.742353, 2.744824, 2.747294, 2.749765, 2.752235, 2.754706, 2.756471, 2.758235, 2.76, 2.761765, 2.763529, 2.765294, 2.767059, 2.769529, 2.772, 2.774471, 2.776941, 2.779412, 2.781471, 2.78353, 2.785588, 2.787647, 2.789706, 2.791765, 2.793824, 2.795882, 2.797941, 2.8, 2.802059, 2.804118, 2.806588, 2.809059, 2.81153, 2.814, 2.816471, 2.818941, 2.821412, 2.823883, 2.826353, 2.828824, 2.830883, 2.832941, 2.835, 2.837059, 2.839118, 2.841177, 2.843647, 2.846118, 2.848588, 2.851059, 2.853529, 2.855294, 2.857059, 2.858824, 2.860588, 2.862353, 2.864118, 2.865882, 2.867941, 2.87, 2.872059, 2.874118, 2.876177, 2.878235, 2.88, 2.881765, 2.883529, 2.885294, 2.887059, 2.888824, 2.890588, 2.892647, 2.894706, 2.896765, 2.898824, 2.900883, 2.902941, 2.905412, 2.907882, 2.910353, 2.912824, 2.915294, 2.917059, 2.918824, 2.920588, 2.922353, 2.924118, 2.925883, 2.927647, 2.929412, 2.931177, 2.932941, 2.934706, 2.936471, 2.938235, 2.94, 2.942059, 2.944118, 2.946177, 2.948236, 2.950294, 2.952353, 2.954118, 2.955883, 2.957647, 2.959412, 2.961176, 2.962941, 2.964706, 2.966765, 2.968824, 2.970882, 2.972941, 2.975, 2.977059, 2.978824, 2.980588, 2.982353, 2.984118, 2.985882, 2.987647, 2.989412, 2.991471, 2.99353, 2.995588, 2.997647, 2.999706, 3.001765, 3.00353, 3.005294, 3.007059, 3.008824, 3.010588, 3.012353, 3.014118, 3.015882, 3.017647, 3.019412, 3.021177, 3.022941, 3.024706, 3.026471, 3.028015, 3.029559, 3.031103, 3.032647, 3.034191, 3.035735, 3.03728, 3.038824, 3.040588, 3.042353, 3.044118, 3.045882, 3.047647, 3.049412, 3.051177, 3.053236, 3.055294, 3.057353, 3.059412, 3.061471, 3.063529, 3.065294, 3.067059, 3.068824, 3.070588, 3.072353, 3.074118, 3.075882, 3.077647, 3.079412, 3.081177, 3.082941, 3.084706, 3.086471, 3.088235, 3.09, 3.091765, 3.093529, 3.095294, 3.097059, 3.098824, 3.100588, 3.102353, 3.104118, 3.105882, 3.107647, 3.109412, 3.111177, 3.112941, 3.119118, 3.137647]


    NOM_RES = 10000
    SER_RES = 9820
    TEMP_NOM = 25
    NUM_SAMPLES = 25
    THERM_B_COEFF = 3950
    ADC_MAX = 1023
    ADC_Vmax = 3.15

    def init_temp_sensor(TENP_SENS_ADC_PIN_NO = constants.TEMP_PIN):
        adc = ADC(Pin(TENP_SENS_ADC_PIN_NO))
        adc.atten(ADC.ATTN_11DB)
        adc.width(ADC.WIDTH_10BIT)
        return adc

    temp_sens = init_temp_sensor()

    def read_temp():
        raw_read = []
        # Collect NUM_SAMPLES
        for i in range(1, NUM_SAMPLES+1):
            raw_read.append(temp_sens.read())

        # Average of the NUM_SAMPLES and look it up in the table
        raw_average = sum(raw_read)/NUM_SAMPLES
        # print('Temp Utils: raw_avg = ' + str(raw_average))
        # print('Temp Utils: V_measured = ' + str(adc_V_lookup[round(raw_average)]))

        # Convert to resistance
        raw_average = ADC_MAX * adc_V_lookup[round(raw_average)]/ADC_Vmax
        resistance = (SER_RES * raw_average) / (ADC_MAX - raw_average)
        # print('Temp Utils: Thermistor resistance: {} ohms'.format(resistance))

        # Convert to temperature
        steinhart  = log(resistance / NOM_RES) / THERM_B_COEFF
        steinhart += 1.0 / (TEMP_NOM + 273.15)
        steinhart  = (1.0 / steinhart) - 273.15
        return steinhart

import utils_read_temp as t
t.read_temp()