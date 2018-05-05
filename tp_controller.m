% Template MATLAB code for reading data from a private channel, analyzing
% the data and storing the analyzed data in another channel.

% Prior to running this MATLAB code template, assign the channel ID to read
% data from to the 'readChannelID' variable. Since this is a private
% channel, also assign the read API Key to the 'readAPIKey' variable. You
% can find the read API Key in the right side pane of this page.

% To store the analyzed data, you will need to write it to a channel other
% than the one you are reading data from. Assign this channel ID to the
% 'writeChannelID' variable. Also assign the write API Key to the
% 'writeAPIKey' variable below. You can find the write API Key in the right
% side pane of this page.

% TODO - Replace the [] with channel ID to read data from:
readChannelID = 466538;
% TODO - Enter the Read API Key between the '' below:
readAPIKey = 'CJGDX5UTPYWD40GE';

% TODO - Replace the [] with channel ID to write data to:
writeChannelID = 489308;
% TODO - Enter the Write API Key between the '' below:
writeAPIKey = 'XIZBXXP2GGNKZGML';

%% Read Data %%
%data = thingSpeakRead(readChannelID, 'ReadKey', readAPIKey,'OutputFormat','table');
% data = thingSpeakRead(readChannelID, 'ReadKey', readAPIKey,'OutputFormat','timetable');

data = thingSpeakRead(readChannelID,'ReadKey', readAPIKey,'Fields',[1,2],'NumMinutes',3,'OutputFormat','table') %to read the data received in a time gap 0f 5 minutes
%the five minutes are important beacuase this code is run every five
%minutes by TIME CONTROL: 'HOSPITAL TIME CONTROL'



%% Analyze Data %%
% Add code in this section to analyze data and store the result in the
% analyzedData variable.
analyzedData = data;
analyzedData
A = table2array(analyzedData(:,2:3))%convert the receives data to an array!!
%all the tranformations and if should be based on 'A', not in data

%% Write Data %%
thingSpeakWrite(writeChannelID, analyzedData, 'WriteKey', writeAPIKey);
%thingSpeakWrite(489308, analyzedData, 'WriteKey', 'XIZBXXP2GGNKZGML');

%to retreive data from channel using a request!
%https://api.thingspeak.com/channels/489308/feeds.json?api_key=XIZBXXP2GGNKZGML