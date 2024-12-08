function list_yellow_images()
  % Hardcoded input directory with wildcard for .jpg files
  input_dir = 'C:\Szkola\SEMESTR7\PO\lab3\yellow\*.jpg';

  % Hardcoded output directory
  output_dir = 'C:\Szkola\SEMESTR7\PO\lab3\mostly_yellow\';

  % Create output directory if it doesn't exist
  if ~exist(output_dir, 'dir')
    mkdir(output_dir);
  end

  % Thresholds for "yellow" in the RGB space
  % Yellow is approximately [R > 200, G > 200, B < 150]
  yellow_threshold = struct('R', 200, 'G', 200, 'B', 150);

  % Get all .jpg files in the input directory
  files = dir(input_dir);

  % Loop through each file
  for i = 1:length(files)
    filename = files(i).name;
    filepath = fullfile(fileparts(input_dir), filename);

    try
      % Read the image
      img = imread(filepath);

      % Check if it's a color image
      if size(img, 3) == 3
        % Extract RGB channels
        R = img(:,:,1);
        G = img(:,:,2);
        B = img(:,:,3);

        % Create a mask for yellow pixels
        yellow_mask = (R > yellow_threshold.R) & ...
                      (G > yellow_threshold.G) & ...
                      (B < yellow_threshold.B);

        % Calculate the proportion of yellow pixels
        yellow_ratio = sum(yellow_mask(:)) / numel(yellow_mask);

        % If the image is mostly yellow, save it to the output directory
        if yellow_ratio > 0.05  % More than 50% yellow
          copyfile(filepath, fullfile(output_dir, filename));
        end
      end
    catch
      fprintf("Warning: Could not process file %s\n", filename);
    end
  end

  fprintf("Processing complete. Mostly yellow images saved to: %s\n", output_dir);
end

