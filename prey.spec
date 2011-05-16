%define name prey
%define version 0.5.3

Name: %{name}
Summary: Prey is a lightweight application for tracking your stolen laptop
Version: %{version}
Release: %mkrel 1
License: GPLv3
Group: Monitoring
Source: http://preyprojetc.com/releases/%{version}/%{name}-%{version}-linux.zip
URL:	http://preyproject.com/
Requires: curl, scrot, groff, streamer, perl-Net-SSLeay, perl-IO-Socket-SSL
BuildRoot: %_tmppath/%{name}-%{version}-buildroot

%description
Prey is a lightweight application for tracking your stolen laptop.

Prey comprises a shell scripts which calls out on a regular basis
to either a server run by prey project, or a url nominated by 
system administration. A graphical configuration tool is also provided
which is used to maintain the simple config file.

%prep
rm -rf %{buildroot}
%setup -n prey

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/

mv * %{buildroot}%{_datadir}/%{name}/

cat << EOF > %buildroot%_sysconfdir/cron.d/%name
 */20 * * * * root /usr/share/prey/prey.sh > /var/log/prey.log
EOF

%files
%defattr(0644,root,root)
%{_datadir}/%{name}
%{_sysconfdir}/cron.d/prey

%clean
rm -rf $RPM_BUILD_ROOT
