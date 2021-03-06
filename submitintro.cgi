#!/usr/bin/perl

use CGI qw/:all/;
use Data::Dumper;  
use CGI::Session;

print header;
my $name = param("name");
my $gender = param("gender");
my $email = param("email");
my $hs = param("highschool");
my $emergencyname = param("emergencyname");
my $emergencynumber = param("emergencynumber");
my $experience = param("experience");
my $year = param("year");
`echo "Hi $name,\n\nThank you for applying at UNSW High School Computing Club.\n\nYou will receive additional information in the coming days. Any queries can be sent to csesoc.computerclub\@cse.unsw.edu.au. Please do not reply to this email directly.\n\nRegards,\nUNSW High School Computing Club\n" | mail -aFrom:no-reply\@cse.unsw.edu.au -s "Computing Club" $email`;

my $postData = "--post-data=\'entry.0.single=$name&entry.6.group=$gender&entry.2.single=$email&entry.3.group=$year&entry.4.single=$hs&entry.5.single=$emergencyname&entry.8.single=$emergencynumber&entry.9.single=$experience\'";
my $response = `wget -q $postData https://docs.google.com/spreadsheet/formResponse?formkey=dHBCSW4yd21CQ3NRT3dhTFhGZjhwVEE6MQ`;
