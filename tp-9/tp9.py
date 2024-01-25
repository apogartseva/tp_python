import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, LSTM   


input = "DAT_XLSX_EURUSD_M1.csv"
df = pd.read_csv(input)
df['date-time'] = pd.to_datetime(df['date-time'])


def visualize_curve():
# graphique 
    plt.figure(figsize=(12, 6))
    plt.plot(df['date-time'], df['close'], label='Valeur finale', color='pink')
    plt.title('Evolution temporelle de la valeur finale EUR/USD Forex')
    plt.xlabel('Dates')
    plt.ylabel('Valeur finale')
    plt.legend()
    plt.show()

# naive prediction
def naive_prediction():

    df['previous_close'] = df['close'].shift(1)
    df['next_close'] = df['close'].shift(-1)



    # predicted direction
    df['direction'] = np.where(df['close'] > df['previous_close'], 1, -1)

    # true direction
    df['true_direction'] = np.where(df['next_close'] > df['close'], 1, -1)

    # success rate
    correct_predictions = (df['direction'] == df['true_direction']).sum()
    total_predictions = len(df)
    success_rate = correct_predictions / total_predictions
    print(f"Taux de réussite de la prédiction naïve: {success_rate * 100:.2f}%")
    df.to_csv('DAT_naive_prediction.csv', index=False)
    print("Les résultats de la prédiction naïve sont dans DAT_naive_prediction.csv")



def cnn1d():
    # colonnes pour l'apprentissage
    features = ['open', 'high', 'low', 'close']

    # normalisation
    scaler = MinMaxScaler()
    df[features] = scaler.fit_transform(df[features])

    # direction = 1 pour hausse, 0 pour baisse (-1 ne foncionne pas ici ??)
    df['target'] = np.where(df['close'].shift(-1) > df['close'], 1, 0)  
    selected_columns = features + ['target']

    sequences = []
    targets = []

    for i in range(len(df) - 120):
        seq = df.iloc[i:i + 120][features].values
        label = df.iloc[i + 120]['target']
        sequences.append(seq)
        targets.append(label)
    X, y = np.array(sequences), np.array(targets)

    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    model = Sequential()
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(120, len(features))))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # entrainemnt
    model.fit(X_train, y_train, epochs=3, batch_size=32, validation_data=(X_val, y_val))

    accuracy = model.evaluate(X_test, y_test)[1]
    print(f"Précision de CNN 1D: {accuracy * 100:.2f}%")

def lstm():
    #meme chose que cnn1d
    features = ['open', 'high', 'low', 'close']
    scaler = MinMaxScaler()
    df[features] = scaler.fit_transform(df[features])    
    df['target'] = np.where(df['close'].shift(-1) > df['close'], 1, 0)
    selected_columns = features + ['target']

    sequences = []
    targets = []

    for i in range(len(df) - 120):
        seq = df.iloc[i:i + 120][features].values
        label = df.iloc[i + 120]['target']
        sequences.append(seq)
        targets.append(label)

    X, y = np.array(sequences), np.array(targets)

    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    # on change le nombre d'échantillons, pas de temps, caractéristiques par rapport au cnn
    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], len(features)))
    X_val = X_val.reshape((X_val.shape[0], X_val.shape[1], len(features)))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], len(features)))
    model = Sequential()
    model.add(LSTM(50, input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_val, y_val))

    accuracy = model.evaluate(X_test, y_test)[1]
    print(f"Précision de LSTM: {accuracy * 100:.2f}%")


# visualize_curve()
# naive_prediction()
# cnn1d()
lstm()
