%define name prey
%define version 0.5.4

Name: %{name}
Summary: Prey is a lightweight application for tracking your stolen laptop
Version: %{version}
Release: %mkrel 3
License: GPLv3
Group: Monitoring
Source0: http://preyproject.com/releases/0.5.4/prey-0.5.4-linux.zip
Source1: prey-config.desktop
URL:	http://preyproject.com/
Requires: curl, scrot, groff, streamer, perl-Net-SSLeay, perl-IO-Socket-SSL, mpg123, imagemagick, traceroute, gksu

%description
Prey is a lightweight application for tracking your stolen laptop.

Prey comprises a shell scripts which calls out on a regular basis
to either a server run by prey project, or a url nominated by 
system administration. A graphical configuration tool is also provided
which is used to maintain the simple config file.

%prep
rm -rf %{buildroot}
%setup -n prey
install -m 755 %{SOURCE1} prey-config.desktop

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
mkdir -p %{buildroot}%{_datadir}/applications/
install -m 755 prey-config.desktop %{buildroot}%{_datadir}/applications/

mv * %{buildroot}%{_datadir}/%{name}/

cat << EOF > %buildroot%_sysconfdir/cron.d/%name
 */20 * * * * root /usr/share/prey/prey.sh > /var/log/prey.log
EOF

%files
%defattr(0755,root,root)
%{_datadir}/%{name}
%{_sysconfdir}/cron.d/prey
%{_datadir}/applications/prey-config.desktop

