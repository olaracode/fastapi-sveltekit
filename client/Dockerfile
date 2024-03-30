# Use the official Node.js image as base
FROM node:latest

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm i

# Copy the rest of the application files
COPY . .

# Expose port 3000 (the default SvelteKit port)
EXPOSE 3000

# Command to run the SvelteKit dev server
CMD ["npm", "run", "dev"]
